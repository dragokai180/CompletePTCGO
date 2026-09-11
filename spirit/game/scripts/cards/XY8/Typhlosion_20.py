from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d4709c1-33b1-512e-b34c-c48ab8dea9e7',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name',
    display_name='Typhlosion',
    searchable_by=['Typhlosion', 'Stage 2', 'Typhlosion'],
    subtypes=['Stage 2'],
    collector_number=20,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name',
    family_id=155,
    abilities=[
        Attack(
            title='Massive Eruption',
            game_text='Discard the top 5 cards of your deck. This attack does 80 damage times the number of Energy cards you discarded.',
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Flare Destroy',
            game_text="Discard an Energy attached to this Pokémon. Then, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
