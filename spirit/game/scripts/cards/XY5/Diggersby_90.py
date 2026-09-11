from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bf2f0637-7c94-5bc1-8a11-1e7cabf9f96e',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name',
    display_name='Diggersby',
    searchable_by=['Diggersby', 'Stage 1', 'Diggersby'],
    subtypes=['Stage 1'],
    collector_number=90,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    family_id=659,
    abilities=[
        Attack(
            title='Ear Dig',
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
