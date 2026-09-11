from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a932946-7973-545b-8d97-3715f42a2024',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name',
    display_name='Tatsugiri',
    searchable_by=['Tatsugiri', 'Basic', 'Tatsugiri'],
    subtypes=['Basic'],
    collector_number=141,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Survival Strategy',
            game_text='Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
