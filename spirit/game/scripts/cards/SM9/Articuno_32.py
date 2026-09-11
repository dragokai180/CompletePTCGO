from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab9d4056-05b7-59ef-ba0d-3c5bdbbcc158',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name',
    display_name='Articuno',
    searchable_by=['Articuno', 'Basic', 'Articuno'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Ability(
            title='Blizzard Veil',
            game_text='As long as this Pokémon is your Active Pokémon, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Water Pokémon.',
            passive=standard_passive('As long as this Pokémon is your Active Pokémon, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Water Pokémon.'),
        ),
        Attack(
            title='Cold Cyclone',
            game_text='Move 2 Water Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
