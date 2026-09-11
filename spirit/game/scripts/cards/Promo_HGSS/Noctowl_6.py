from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7c6be74-ff61-5b1c-994e-a0cbd59d6de1',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name',
    display_name='Noctowl',
    searchable_by=['Noctowl', 'Stage 1', 'Noctowl'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'HGSS06'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    family_id=163,
    abilities=[
        Ability(
            title='Night Scope',
            game_text="Once during your turn (before your attack), you may look at your opponent's hand. This power can't be used if Noctowl is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hypnoblast',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
