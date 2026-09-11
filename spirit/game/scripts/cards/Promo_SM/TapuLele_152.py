from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9ec63b8-9a6d-5f19-948f-f572ddd7032e',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name',
    display_name='Tapu Lele',
    searchable_by=['Tapu Lele', 'Basic', 'TapuLele'],
    subtypes=['Basic'],
    collector_number=152,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=786,
    abilities=[
        Ability(
            title='Charmed Charm',
            game_text='Whenever you attach a Pokémon Tool card that has "Fairy Charm" in its name from your hand to this Pokémon during your turn, you may leave your opponent\'s Active Pokémon Confused.',
            passive=standard_passive('Whenever you attach a Pokémon Tool card that has "Fairy Charm" in its name from your hand to this Pokémon during your turn, you may leave your opponent\'s Active Pokémon Confused.'),
        ),
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
