from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18522fa6-a1e0-5222-b6c9-ad4ad7d421dd',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name',
    display_name='Toxicroak',
    searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    family_id=453,
    abilities=[
        Attack(
            title='Poison Jab',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Exact Revenge',
            game_text="If any of your Psychic Pokémon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
