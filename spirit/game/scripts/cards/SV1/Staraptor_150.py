from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cabbcf20-0d01-5e17-8758-33b31bae51d5',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name',
    display_name='Staraptor',
    searchable_by=['Staraptor', 'Stage 2', 'Staraptor'],
    subtypes=['Stage 2'],
    collector_number=150,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name',
    family_id=396,
    abilities=[
        Attack(
            title='Tailspin Away',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
