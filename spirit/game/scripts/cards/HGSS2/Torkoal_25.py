from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e0732b9-d233-565c-a7ac-8134cc1c2503',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name',
    display_name='Torkoal',
    searchable_by=['Torkoal', 'Basic', 'Torkoal'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=324,
    abilities=[
        Ability(
            title='Hot Snort',
            game_text='Once during your turn, when you put Torkoal from your hand onto your Bench, you may flip a coin. If heads, the Defending Pokémon is now Burned.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
