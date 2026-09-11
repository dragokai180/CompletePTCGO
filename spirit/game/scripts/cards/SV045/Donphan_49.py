from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7afeb447-e23a-5605-98b5-554cd0fe36d2',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name',
    display_name='Donphan',
    searchable_by=['Donphan', 'Stage 1', 'Donphan'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    family_id=231,
    abilities=[
        Attack(
            title='Cragalanche',
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Powerful Spin',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
