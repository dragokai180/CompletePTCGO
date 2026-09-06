from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.session.effects import is_special_energy

card = PokemonCardDef(
    guid="8597ac47-5cc3-5283-aab3-e517b28f6eb3",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot","Basic","Hoothoot"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=163,
    abilities=[
        Ability(
            title="Insomnia",
            game_text="This Pokémon can't be Asleep.",
            passive=condition_immunity_passive(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
