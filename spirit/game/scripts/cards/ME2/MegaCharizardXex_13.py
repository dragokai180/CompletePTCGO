from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def inferno_x(ctx):
    """Discard any amount of Fire Energy from among your Pokémon, and this
    attack does 90 damage for each card you discarded in this way."""
    fire = [
        energy
        for pokemon in ctx.my_pokemon_in_play()
        for energy in ctx.attached_energies(pokemon)
        if energy_provides_type(energy, PokemonTypes.FIRE.value)
    ]
    discarded = []
    if fire:
        discarded = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Choose any amount of Fire Energy to discard",
        )
        if discarded:
            await ctx.discard_cards(discarded)
    amount = 90 * len(discarded)
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="d71e5886-0270-5e72-9fc8-b3d334e7392a",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardXex.Name",
    display_name="Mega Charizard X ex",
    searchable_by=["Mega Charizard X ex","Stage 2","ex","SV_Mega","MegaCharizardXex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=13,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    family_id=4,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    abilities=[
        Attack(
            title="Inferno X",
            game_text="Discard any amount of Fire Energy from among your Pokémon, and this attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=90,
            damage_operator="x",
            effect=inferno_x,
        ),
    ],
)
