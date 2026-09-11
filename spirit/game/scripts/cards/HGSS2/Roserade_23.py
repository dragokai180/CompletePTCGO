from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0460ae2d-53e1-5634-8f5c-cbb00c23c825',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name',
    display_name='Roserade',
    searchable_by=['Roserade', 'Stage 1', 'Roserade'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name',
    family_id=315,
    abilities=[
        Ability(
            title='Energy Signal',
            game_text="When you attach a Grass Energy card or Psychic Energy card from your hand to Roserade during your turn, you may use this power. If you attach a Grass Energy card, the Defending Pokémon is now Confused. If you attach a Psychic Energy card, the Defending Pokémon is now Poisoned. This power can't be used if Roserade is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=standard_passive("When you attach a Grass Energy card or Psychic Energy card from your hand to Roserade during your turn, you may use this power. If you attach a Grass Energy card, the Defending Pokémon is now Confused. If you attach a Psychic Energy card, the Defending Pokémon is now Poisoned. This power can't be used if Roserade is affected by a Special Condition."),
        ),
        Attack(
            title='Power Blow',
            game_text='Does 20 damage times the amount of Energy attached to Roserade.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
