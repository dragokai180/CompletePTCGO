from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64fee633-2f17-5b12-a74f-124ca180d90c',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name',
    display_name='Elekid',
    searchable_by=['Elekid', 'Basic', 'Elekid'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=239,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Elekid is Asleep, prevent all damage done to Elekid by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Elekid is Asleep, prevent all damage done to Elekid by attacks.'),
        ),
        Attack(
            title='Sparking Ball',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance. Elekid is now Asleep.",
            cost={},
            effect=standard_attack,
        ),
    ],
)
