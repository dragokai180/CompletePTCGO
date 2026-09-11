from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="f60df7ff-8cec-5f37-9ba2-5a1e1686d664",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigirafex.Name",
    display_name="Farigiraf ex",
    searchable_by=["Farigiraf ex", "Stage 1", "Tera", "ex", "Farigirafex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=108,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Ability(
            title="Armor Tail",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon ex.",
            passive=standard_passive("Prevent all damage done to this Pokémon by attacks from your opponent's Basic Pokémon ex."),
        ),
        Attack(
            title="Dirty Beam",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
