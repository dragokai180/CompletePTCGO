from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37739065-a052-53cc-ab3e-a91329c92af7',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name',
    display_name='Gourgeist',
    searchable_by=['Gourgeist', 'Stage 1', 'Gourgeist'],
    subtypes=['Stage 1'],
    collector_number=78,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    family_id=710,
    abilities=[
        Ability(
            title='Startling Pumpkin',
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, discard 2 random cards from your opponent's hand.",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, discard 2 random cards from your opponent's hand."),
        ),
        Attack(
            title='Shadow Bind',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
