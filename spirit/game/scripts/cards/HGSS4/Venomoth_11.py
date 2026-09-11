from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d88df1d0-422e-5334-8be3-1fd3b601f5e8',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name',
    display_name='Venomoth',
    searchable_by=['Venomoth', 'Stage 1', 'Venomoth'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    family_id=48,
    abilities=[
        Ability(
            title='Poison Moth Wind',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, your opponent's Active Pokémon is now Poisoned. If tails, your Active Pokémon is now Poisoned. This power can't be used if Venomoth is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Stun Spore',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
