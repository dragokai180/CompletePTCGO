from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a77e62ca-4f56-5b7d-8077-9e7e97f45e4b',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name',
    display_name='Solgaleo',
    searchable_by=['Solgaleo', 'Stage 2', 'Solgaleo'],
    subtypes=['Stage 2'],
    collector_number=87,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    family_id=791,
    abilities=[
        Attack(
            title='Shining Arrow',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fangs of the Sunne',
            game_text="This Pokémon can't use Fangs of the Sunne during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
