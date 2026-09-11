from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe80c89a-0eb7-5af6-bf8a-eaeb5ee436b2',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    display_name='Pupitar',
    searchable_by=['Pupitar', 'Stage 1', 'Pupitar'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    family_id=246,
    abilities=[
        Ability(
            title='Boost Gas',
            game_text='If Pupitar has any Energy attached to it, the Retreat Cost of Pupitar is 0.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('If Pupitar has any Energy attached to it, the Retreat Cost of Pupitar is 0.'),
        ),
        Attack(
            title='Rage',
            game_text='Does 20 damage plus 10 more damage for each damage counter on Pupitar.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
