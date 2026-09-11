from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c743c0f-90d9-5087-adee-2a13a99b04ca',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name',
    display_name='Oinkologne',
    searchable_by=['Oinkologne', 'Stage 1', 'Oinkologne'],
    subtypes=['Stage 1'],
    collector_number=184,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    family_id=915,
    abilities=[
        Attack(
            title='Finest Selection',
            game_text='Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Perfume Press',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
