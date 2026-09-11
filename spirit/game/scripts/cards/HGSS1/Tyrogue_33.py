from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7261d67c-57cf-55fe-8527-907111f32d52',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name',
    display_name='Tyrogue',
    searchable_by=['Tyrogue', 'Basic', 'Tyrogue'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=236,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Tyrogue is Asleep, prevent all damage done to Tyrogue by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Tyrogue is Asleep, prevent all damage done to Tyrogue by attacks.'),
        ),
        Attack(
            title='Mischievous Punch',
            game_text="This attack's damage isn't affected by Weakness or Resistance. Tyrogue is now Asleep.",
            cost={},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
