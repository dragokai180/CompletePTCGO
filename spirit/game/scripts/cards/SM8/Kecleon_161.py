from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='653a6e39-d0f9-5892-b1e6-153d3e35f770',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name',
    display_name='Kecleon',
    searchable_by=['Kecleon', 'Basic', 'Kecleon'],
    subtypes=['Basic'],
    collector_number=161,
    set_code='SM8',
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
            title='Unit Color 1',
            game_text='As long as this Pokémon has Unit Energy GrassFireWater attached to it, it is a Grass, Fire, and Water Pokémon.',
            passive=standard_passive('As long as this Pokémon has Unit Energy GrassFireWater attached to it, it is a Grass, Fire, and Water Pokémon.'),
        ),
        Attack(
            title='Tongue Smack',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
