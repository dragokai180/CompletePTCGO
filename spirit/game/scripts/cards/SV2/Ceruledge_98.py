from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='17e837e0-8ae0-549e-9ca0-d8ed14bb31e6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name',
    display_name='Ceruledge',
    searchable_by=['Ceruledge', 'Stage 1', 'Ceruledge'],
    subtypes=['Stage 1'],
    collector_number=98,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    family_id=935,
    abilities=[
        Attack(
            title='Life Sucker',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Fighting Sword',
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
