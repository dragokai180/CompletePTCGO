from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='531bd232-1509-589e-9c78-268e42227539',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name',
    display_name='Charizard',
    searchable_by=['Charizard', 'Stage 2', 'Charizard'],
    subtypes=['Stage 2'],
    collector_number=105,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Recall',
            game_text="Choose 1 of this Pokémon's attacks from its previous Evolutions and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Combustion Blast',
            game_text="This Pokémon can't use Combustion Blast during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
