from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f9802e5e-17df-5b87-9a03-1045154fecb3',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BronzongBREAK.Name',
    display_name='Bronzong BREAK',
    searchable_by=['Bronzong BREAK', 'BREAK', 'BronzongBREAK'],
    subtypes=['BREAK'],
    collector_number=62,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name',
    family_id=436,
    abilities=[
        Attack(
            title='Metal Rain',
            game_text="Discard as many Metal Energy attached to this Pokémon as you like. For each Energy card discarded in this way, choose 1 of your opponent's Pokémon and do 30 damage to it. Don't apply Weakness and Resistance. (You may choose the same Pokémon more than once.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
