from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c542bb58-5a9b-52c7-937b-9f1125a5af01',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name',
    display_name='Pichu',
    searchable_by=['Pichu', 'Basic', 'Pichu'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=172,
    abilities=[
        Ability(
            title='Sweet Sleeping Face',
            game_text='As long as Pichu is Asleep, prevent all damage done to Pichu by attacks.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Pichu is Asleep, prevent all damage done to Pichu by attacks.'),
        ),
        Attack(
            title='Playground',
            game_text='Each player may search his or her deck for as many Basic Pokémon as he or she likes, put them onto his or her Bench, and shuffle his or her deck afterward. (You put your Pokémon on the Bench first.) Pichu is now Asleep.',
            cost={},
            effect=standard_attack,
        ),
    ],
)
