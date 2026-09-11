from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01cfb2a3-f905-5c36-9f59-43d08d646dc9',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name',
    display_name='Kecleon',
    searchable_by=['Kecleon', 'Basic', 'Kecleon'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=352,
    abilities=[
        Ability(
            title='Unit Color 2',
            game_text='As long as this Pokémon has Unit Energy LightningPsychicMetal attached to it, it is a Lightning, Psychic, and Metal Pokémon.',
            passive=standard_passive('As long as this Pokémon has Unit Energy LightningPsychicMetal attached to it, it is a Lightning, Psychic, and Metal Pokémon.'),
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
