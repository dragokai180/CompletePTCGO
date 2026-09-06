from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.pokemon import TeraRulePassive


async def onyx(ctx):
    """Discard all Energy from this Pokémon, and take a Prize card."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.discard_cards(energies)
    await ctx.take_prizes(1)


card = PokemonCardDef(
    guid="e64ec7a6-ee78-5a63-bba8-e54bdb42103e",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name",
    display_name="Umbreon ex",
    searchable_by=["Umbreon ex","Stage 1","ex","Tera","Umbreonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=60,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Moon Mirage",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Onyx",
            game_text="Discard all Energy from this Pokémon, and take a Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=onyx,
        ),
    ],
)
