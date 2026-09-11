from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9bcd06ba-9d3a-5c2a-9cfa-2afad9e850d9',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name',
    display_name='Haxorus',
    searchable_by=['Haxorus', 'Stage 2', 'Haxorus'],
    subtypes=['Stage 2'],
    collector_number=111,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name',
    family_id=610,
    abilities=[
        Attack(
            title='Dragon Dance',
            game_text="As long as this Haxorus is your Active Pokémon, each of its attacks does 100 more damage (before applying Weakness and Resistance). You can't add more than 100 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 3 cards of your deck.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
