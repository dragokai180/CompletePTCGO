from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2e0e47f-5904-597f-a12a-83212806f05e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name',
    display_name='Noctowl',
    searchable_by=['Noctowl', 'Stage 1', 'Noctowl'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    family_id=163,
    abilities=[
        Ability(
            title='Night Sight',
            game_text="Once during your turn (before your attack), you may draw a card. This power can't be used if Noctowl is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Extrasensory',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 40 damage plus 40 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
