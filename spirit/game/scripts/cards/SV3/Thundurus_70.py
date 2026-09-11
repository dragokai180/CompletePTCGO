from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efa17d72-16d5-5828-b664-dcd8752302d8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name',
    display_name='Thundurus',
    searchable_by=['Thundurus', 'Basic', 'Thundurus'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=642,
    abilities=[
        Ability(
            title='Adverse Weather',
            game_text="As long as this Pokémon is in the Active Spot, prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon."),
        ),
        Attack(
            title='Gigantic Bolt',
            game_text='This Pokémon also does 90 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
