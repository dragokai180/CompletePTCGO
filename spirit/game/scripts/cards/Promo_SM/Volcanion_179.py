from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ecd53342-890c-5fca-9d11-a0ec65c47e3e',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name',
    display_name='Volcanion',
    searchable_by=['Volcanion', 'Basic', 'Volcanion'],
    subtypes=['Basic'],
    collector_number=179,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Attack(
            title='Flare Starter',
            game_text="Search your deck for a Fire Energy card and attach it to 1 of your Pokémon. If you go second and it's your first turn, instead search for up to 3 Fire Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='High-Heat Blast',
            game_text='If you have at least 4 Fire Energy in play, this attack does 60 more damage.',
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
