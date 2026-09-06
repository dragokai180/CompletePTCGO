from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_special_energy
from spirit.game.session.effects import is_special_energy


async def enhanced_hammer(ctx):
    """Discard a Special Energy from 1 of your opponent's Pokémon."""
    energies = [
        energy
        for pokemon in ctx.opponent_pokemon_in_play()
        for energy in ctx.attached_energies(pokemon)
        if is_special_energy(energy)
    ]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Special Energy to discard.",
    )
    await ctx.discard_cards(picks)


card = ItemCardDef(
    guid="e48bbe66-e693-5a68-a99f-14d6428ad935",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer","Item","EnhancedHammer"],
    subtypes=["Item"],
    collector_number=148,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=enhanced_hammer,
    condition=opponent_has_special_energy,
)
