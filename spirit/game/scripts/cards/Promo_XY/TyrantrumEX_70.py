from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4878d363-3f3e-52f4-a3c7-ba3c810437fb',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TyrantrumEX.Name',
    display_name='Tyrantrum-EX',
    searchable_by=['Tyrantrum-EX', 'Basic', 'EX', 'TyrantrumEX'],
    subtypes=['Basic', 'EX'],
    collector_number=70,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=697,
    abilities=[
        Ability(
            title='Despotic Fang',
            game_text="Damage from this Pokémon's attacks isn't affected by any effects on your opponent's Active Pokémon.",
            passive=standard_passive("Damage from this Pokémon's attacks isn't affected by any effects on your opponent's Active Pokémon."),
        ),
        Attack(
            title='Dragon Fang',
            game_text='Discard 3 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
