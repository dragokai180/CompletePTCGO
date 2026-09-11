from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="b62c3393-f99c-535c-9cff-3b15d8a1e429",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "Tera", "ex", "Revavroomex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=15,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Attack(
            title="Accelerator Flash",
            game_text="If this Pokémon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Shattering Speed",
            game_text="Discard this Pokémon and all attached cards.",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
