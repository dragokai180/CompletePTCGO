from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="6c40d118-1c62-5e89-b5a6-4674519b1410",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrioex.Name",
    display_name="Wugtrio ex",
    searchable_by=["Wugtrio ex", "Stage 1", "Tera", "ex", "Wugtrioex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=60,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Attack(
            title="Tricolor Pump",
            game_text="Discard up to 3 Energy cards from your hand. This attack does 60 damage to 1 of your opponent's Pokémon for each Energy card you discarded in this way. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Numbing Hold",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
