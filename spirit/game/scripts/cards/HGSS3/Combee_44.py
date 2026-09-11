from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fb354c12-032a-5970-b0aa-f0de638e1ab2',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    display_name='Combee',
    searchable_by=['Combee', 'Basic', 'Combee'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=415,
    abilities=[
        Attack(
            title='Enraged Assault',
            game_text='If Vespiquen is on your Bench and has any damage counters on it, this attack does 20 damage plus 60 more damage and the Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
