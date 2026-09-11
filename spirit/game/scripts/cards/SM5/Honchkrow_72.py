from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df5e8ab0-f74a-5278-b211-4fe6be951ec3',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name',
    display_name='Honchkrow',
    searchable_by=['Honchkrow', 'Stage 1', 'Honchkrow'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    family_id=198,
    abilities=[
        Attack(
            title='Rip and Run',
            game_text="Discard a random card from your opponent's hand. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
