from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1fac6266-7fb4-5976-a850-e6e3882a98c2',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name',
    display_name='Corvisquire',
    searchable_by=['Corvisquire', 'Stage 1', 'Corvisquire'],
    subtypes=['Stage 1'],
    collector_number=165,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name',
    family_id=821,
    abilities=[
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Clutch',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
