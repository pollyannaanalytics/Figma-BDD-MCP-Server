from typing import Any
import logging

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from typing import Any
import logging
import os
import httpx

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('figma_service')


FIGMA_API_BASE = "https://api.figma.com/v1"

# Load environment variables
load_dotenv()

# Initialize FastMCP server


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('bdd_generator_mcp')

mcp = FastMCP("bdd-generator-mcp")


@mcp.prompt(
    name = "generate bdd test plan from figma",
    description="generate BDD test plan from figma"
)
async def generate_bdd_from_figma(url: str) -> Any:
    """Generate BDD test plan from Figma URL
    
    Args:
        url (str): Figma design URL
        
    Returns:
        str: Generated BDD test plan in Gherkin syntax
    """
    try:
        file_key, node_id = await extract_figma_info(url)
        design_data = await get_figma_data(file_key, node_id)
        
        # generate BDD test plan
        prompt = f"""
        Based on the following Figma design data, create a comprehensive BDD (Behavior Driven Development) test plan.
        
        Analyze the UI elements and generate scenarios for:
        1. Layout and Visual Elements:
           - Presence and visibility of components
           - Layout structure and hierarchy
           - Responsive design behavior
        
        2. User Interactions:
           - Click events and navigation
           - Form inputs and validation
           - Error states and messages
        
        3. Business Logic:
           - User flows and journeys
           - Data display and updates
           - State management
        
        Design Data:
        {design_data}
        
        Please format the response in Gherkin syntax with:
        - Feature: [Feature name]
        - Scenario: [Scenario description]
          Given [initial context]
          When [action occurs]
          Then [expected outcome]
        """
        
        return prompt

    except Exception as e:
        logger.error(f"Error in generate_bdd_from_figma: {e}")
        return f"Error generating BDD test plan: {str(e)}"
    

# figma api

async def extract_figma_info(url: str) -> tuple[str, str | None]:
    """Extract file key and node id from Figma URL"""
    try:
        file_key = url.split("/design/")[1].split("/")[0]
        node_id = url.split("node-id=")[1] if "node-id=" in url else None
        logger.debug("file_key: " + file_key)
        logger.debug("node_id: " + node_id)
        return file_key, node_id
    except Exception as e:
        logger.error(f"Error parsing Figma URL: {e}")
        raise ValueError("Invalid Figma URL format")

async def get_figma_data(file_key: str, node_id: str | None = None) -> dict[str, Any]:
    """Get Figma file data using Figma API"""
    try:
        headers = {
        "X-Figma-Token": os.getenv("FIGMA_API_TOKEN")
        }

        url = f"{FIGMA_API_BASE}/files/{file_key}"
        if node_id:
            url += f"/nodes?ids={node_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

    except Exception as e:
        logger.error(f"Error fetching Figma data: {e}")
        raise Exception(f"Failed to fetch Figma data: {str(e)}")







if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
        