from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="40fef035-6e24-51ef-8baf-01f43055bdae",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name",
    display_name="Umbreon ex",
    searchable_by=["Umbreon ex", "Stage 1", "ex", "Tera", "Umbreonex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=176,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Moon Mirage",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title="Onyx",
            game_text="Discard all Energy from this Pokémon, and take a Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
