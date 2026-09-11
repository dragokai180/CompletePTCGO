from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='095b43c1-7b66-5676-9bdc-ef0b5795a229',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dachsbun.Name',
    display_name='Dachsbun',
    searchable_by=['Dachsbun', 'Stage 1', 'Dachsbun'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name',
    family_id=926,
    abilities=[
        Ability(
            title='Well-Baked Body',
            game_text="This Pokémon can't be Burned. Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon.",
            passive=standard_passive("This Pokémon can't be Burned. Prevent all damage done to this Pokémon by attacks from your opponent's Fire Pokémon."),
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
