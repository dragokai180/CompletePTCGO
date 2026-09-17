from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.scripts.cards.ME1.Lunatone_74 import (
    lunar_cycle, lunar_cycle_condition,
)


card = PokemonCardDef(
    guid="c525073e-1343-5320-9fc4-4563129f3b4d",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    abilities=[
        Ability(
            title="Lunar Cycle",
            game_text="Once during your turn, if you have Solrock in play, you may discard a Basic [ [Fighting] ] Energy card from your hand in order to use this Ability. Draw 3 cards. You can't use more than 1 Lunar Cycle Ability each turn.",
            effect=lunar_cycle,
            condition=lunar_cycle_condition,
            shared_once_per_turn="Lunar Cycle",
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)
