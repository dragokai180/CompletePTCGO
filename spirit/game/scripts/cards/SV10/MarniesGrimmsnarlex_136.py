from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_marnies(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Marnie's ")


def _is_basic_darkness_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.DARKNESS.value in types


async def punk_up(ctx):
    """On evolve: you may search for up to 5 Basic Darkness Energy and attach
    them to your Marnie's Pokémon in any way you like."""
    if not await ctx.ask_yes_no(
        "Search your deck for up to 5 Basic Darkness Energy cards?"
    ):
        return
    await search_attach_energy(
        _is_basic_darkness_energy, count=5, target_pred=_is_marnies,
        prompt="Choose up to 5 Basic Darkness Energy cards to attach.",
    )(ctx)


async def shadow_bullet(ctx):
    await ctx.deal_damage()
    await snipe_attack(30, pool="bench", count=1)(ctx)


card = PokemonCardDef(
    guid="f4bfdd15-0b45-5617-8a88-e849b7a6e0a9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesGrimmsnarlex.Name",
    display_name="Marnie's Grimmsnarl ex",
    searchable_by=["Marnie's Grimmsnarl ex", "Stage 2", "ex", "MarniesGrimmsnarlex"],
    subtypes=["Stage 2", "ex"],
    collector_number=136,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorgrem.Name",
    family_id=859,
    abilities=[
        Ability(
            title="Punk Up",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 5 Basic Darkness Energy cards and attach them to your Marnie's Pokémon in any way you like. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=punk_up,
        ),
        Attack(
            title="Shadow Bullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2},
            damage=180,
            effect=shadow_bullet,
        ),
    ],
)
