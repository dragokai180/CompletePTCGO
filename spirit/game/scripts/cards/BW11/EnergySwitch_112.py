from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card

def energy_switch_condition(board, player_id):
    pokemon = board.pokemon_in_play(player_id)
    if len(pokemon) < 2:
        return False
    return any(any(is_basic_energy_card(e) for e in p.children) for p in pokemon)
async def energy_switch(ctx):
    """Move a basic Energy from 1 of your Pokemon to another of your Pokemon.
    You may play as many Item cards as you like during your turn (before
    your attack)."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(
        pokemon, pokemon, predicate=is_basic_energy_card, max_count=1
    )
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="5f72f28f-27d0-56b3-9cfb-1e9b39fbd7fe",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch","Item","EnergySwitch"],
    subtypes=["Item"],
    collector_number=112,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    effect=energy_switch,
    condition=energy_switch_condition
)
