from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49e117c1-7dcc-56ab-8492-4adf1b30eadb',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name',
    display_name='Celebi',
    searchable_by=['Celebi', 'Basic', 'Celebi'],
    subtypes=['Basic'],
    collector_number=224,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=251,
    abilities=[
        Attack(
            title='Call for Greatness',
            game_text='Search your deck for up to 3 Pokémon-GX with different names, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
