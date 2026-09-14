from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d66d29ab-d322-5c9f-b9f0-60cd8ddf9746',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    display_name='Shaymin',
    searchable_by=['Shaymin', 'Basic', 'Shaymin'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=492,
    abilities=[
        Ability(
            title='Celebration Wind',
            game_text='Once during your turn, when you put Shaymin from your hand onto your Bench, you may move as many Energy cards attached to your Pokémon as you like to any of your other Pokémon.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Energy Bloom',
            game_text='Remove 3 damage counters from each of your Pokémon that has any Energy attached to it.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
