from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7bc29c6f-64de-5961-ad78-48022b9a6c1b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name',
    display_name='Medicham',
    searchable_by=['Medicham', 'Stage 1', 'Medicham'],
    subtypes=['Stage 1'],
    collector_number=111,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    family_id=307,
    abilities=[
        Attack(
            title='Acu-Punch-Ture',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Kick Shot',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
