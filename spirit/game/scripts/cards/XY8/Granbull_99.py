from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='710bf233-4a6a-5c1f-a4a8-47b22e628824',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Granbull.Name',
    display_name='Granbull',
    searchable_by=['Granbull', 'Stage 1', 'Granbull'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    family_id=209,
    abilities=[
        Attack(
            title='Startling Bark',
            game_text="Flip a coin. If heads, choose 3 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Tantrum',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
