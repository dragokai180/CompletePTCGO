from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f677241-a15c-5aca-96aa-6e29db97f604',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name',
    display_name='Feraligatr',
    searchable_by=['Feraligatr', 'Stage 2', 'Feraligatr'],
    subtypes=['Stage 2'],
    collector_number=17,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name',
    family_id=158,
    abilities=[
        Attack(
            title='Hyper Whirlpool',
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Second Strike',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
