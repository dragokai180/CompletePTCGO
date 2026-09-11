from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c99e8ffc-d3dd-515a-93ed-c1bdfd353634',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MandibuzzBREAK.Name',
    display_name='Mandibuzz BREAK',
    searchable_by=['Mandibuzz BREAK', 'BREAK', 'MandibuzzBREAK'],
    subtypes=['BREAK'],
    collector_number=182,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name',
    family_id=630,
    abilities=[
        Attack(
            title='Wings of Disaster',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. Don't apply Weakness and Resistance. Discard all Pokémon Tool cards attached to each of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
