from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2033e680-f6c1-5611-a8c0-f5443ce6be46',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name',
    display_name='Toxapex',
    searchable_by=['Toxapex', 'Stage 1', 'Toxapex'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    family_id=747,
    abilities=[
        Ability(
            title='Toxic Spikes',
            game_text="Whenever your opponent's Active Pokémon retreats, their new Active Pokémon is Poisoned.",
            passive=standard_passive("Whenever your opponent's Active Pokémon retreats, their new Active Pokémon is Poisoned."),
        ),
        Attack(
            title='Venoshock',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
